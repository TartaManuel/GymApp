# nu mai folosim asta I guess
# from django.http import HttpResponse

# pentru redirectionare in pagina
from django.shortcuts import redirect
# pentru lista de parcurs, o lista de componente
from django.views.generic.list import ListView
# vedem daca folosim asta
from django.views.generic.detail import DetailView
# folosim FormView pentru register
# asta le folosim in clase diferite. De exemplu sa dam update la modele diferite, adica tabele diferite
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# pentru redirectare useri la o alta pagina
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# Pentru a nu putea accesa pagina principala decat daca esti logat
from django.contrib.auth.mixins import LoginRequiredMixin
# presupun ca pentru a adauga un user
from django.contrib.auth.forms import UserCreationForm
# asta nu stiu exact ce este, vedem
from django.contrib.auth import login

# aici importam modelele
from .models import ClasaPrincipala, Workout

from datetime import date


# def testList(request):
# return HttpResponse('Avem o lista')

class CustomLoginView(LoginView):
    # doar numele cu html, sa il dam cum vrem
    template_name = 'base/login.html'
    # fieldurile pe care le vrem, le luam pe toate din LoginView
    fields = '__al__'
    # default e false, daca un user e logat deja, nu poate accesa pagina asta sa se logheze din nou
    redirect_authenticated_user = True

    # suprascriem metoda pentru redirectionare, o sa o apelam functia candva
    def get_success_url(self):
        # daca este admin
        if self.request.user.username == "Administrator":
            return reverse_lazy('paginaPrincipala')
        else:
            return reverse_lazy('paginaPrincipalaUser')


class CustomRegisterView(FormView):
    template_name = 'base/register.html'
    # un template care contine 2 textfields, si niste label-uri, il avea deja Django
    form_class = UserCreationForm
    redirect_authenticated_user = True
    # dupa ce dai register, trebuie direct sa mergi la pagina principala I fuess
    success_url = reverse_lazy('paginaPrincipala')

    def form_valid(self, form):
        # dupa ce dam register, bagam userul direct logat
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CustomRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        # daca suntem autentificati deja, ne duce la pagina principala
        # sa nu mai dam register cand suntem logati deja
        if self.request.user.is_authenticated:
            return redirect('paginaPrincipala')
        # daca nu suntem autentificati, ne continuam treaba, interesant, practic e apelul functiei asteia
        return super(CustomRegisterView, self).get(*args, **kwargs)


# Acum facem asta sa fie clasa
class PaginaPrincipalaView(LoginRequiredMixin, ListView):
    model = ClasaPrincipala
    context_object_name = 'ListaPrincipala'
    template_name = 'base/paginaPrincipala.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # filtram in functie de ceva
        # context['ListaPrincipala'] = context['ListaPrincipala'].filter(user=self.request.user)

        # context['count'] = context['ListaPrincipala'].filter(complete=False).count()
        # daca nu dam search, va fi ''
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['ListaPrincipala'] = context['ListaPrincipala'].filter(oraInceput__icontains=search_input)
            # title__icontains nu e predefinit, merge si description__icontains, cred ca doar __icontains e predefinit
            # exista si __startswith sau ceva de genul

        context['search_input'] = search_input
        # numele 'search_input' e ceea ce vrem sa folosim in html. Numele trebuie sa fie acelasi aici si in html acolo
        # la value

        # context e un fel de dictionar. Pe o pozitie avem elementele din lista noastra (taskurile, itemele, elementele
        # din tabela). Pe cealalta pozitie
        # Facem filter prima data ca sa le avem doar cele pentru acest user dupa dam filter in functie de ce vrem sa dam
        # search, adica la ce dam get din acel textfield
        # in context pe a doua pozitie, punem search_input ca sa il pastram si asa nu se sterge din textfield
        return context

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')
        return super(PaginaPrincipalaView, self).get(*args, **kwargs)


class CustomDetailView1(LoginRequiredMixin, DetailView):
    model = ClasaPrincipala
    context_object_name = 'PentruAfisare'
    template_name = 'base/afisare.html'


# acum o sa creat chestii
# ia un model si creeaza toate field-urile
class CustomCreateView1(LoginRequiredMixin, CreateView):

    # dam un request plus cream un item
    model = ClasaPrincipala
    template_name = 'base/create_update.html'
    # fields = '__all__' #asa folosim toate taskurile
    fields = '__all__'
    success_url = reverse_lazy('paginaPrincipala')

    # vrem ca atunci cand cream un item, sa nu trebuiasca sa alegem pentru ce user facem, sa fie doar in userul anume
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CustomCreateView1, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')
        return super(CustomCreateView1, self).get(*args, **kwargs)


class CustomUpdateView1(LoginRequiredMixin, UpdateView):
    # dam un request plus cream un item
    model = ClasaPrincipala
    template_name = 'base/create_update.html'
    # fields = '__all__' #asa folosim toate taskurile
    fields = '__all__'
    # cred ca cand dam submit, daca totul merge bine ne intoarcem la pagina
    # principala
    success_url = reverse_lazy('paginaPrincipala')

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')
        return super(CustomUpdateView1, self).get(*args, **kwargs)


class CustomDeleteView1(LoginRequiredMixin, DeleteView):
    # dam un request plus cream un item
    model = ClasaPrincipala
    template_name = 'base/delete.html'
    context_object_name = 'DeleteItem'
    # cred ca cand dam submit, daca totul merge bine ne intoarcem la pagina
    # principala
    success_url = reverse_lazy('paginaPrincipala')

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')
        return super(CustomDeleteView1, self).get(*args, **kwargs)


class PaginaWorkoutView(LoginRequiredMixin, ListView):
    model = Workout
    context_object_name = 'ListaWorkout'
    template_name = 'base/workoutPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['ListaWorkout'] = context['ListaWorkout'].filter(date__icontains=search_input)
        context['search_input'] = search_input

        success_url = reverse_lazy('paginaPrincipala')

        return context

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')
        return super(PaginaWorkoutView, self).get(*args, **kwargs)


class CustomCreateView2(LoginRequiredMixin, CreateView):

    model = Workout
    template_name = 'base/create_updateWorkout.html'
    fields = '__all__'
    success_url = reverse_lazy('workoutPage')

    # def form_valid(self, form):
    #    form.instance.user = self.request.user
    #    return super(CustomCreateView2, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')
        return super(CustomCreateView2, self).get(*args, **kwargs)


class CustomUpdateView2(LoginRequiredMixin, UpdateView):
    model = Workout
    template_name = 'base/create_updateWorkout.html'
    fields = '__all__'
    success_url = reverse_lazy('workoutPage')

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')
        return super(CustomUpdateView2, self).get(*args, **kwargs)


class CustomDeleteView2(LoginRequiredMixin, DeleteView):
    model = Workout
    template_name = 'base/deleteWorkout.html'
    context_object_name = 'DeleteItem'
    success_url = reverse_lazy('workoutPage')

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')
        return super(CustomDeleteView2, self).get(*args, **kwargs)


class PaginaUserView(LoginRequiredMixin, ListView):
    model = ClasaPrincipala
    context_object_name = 'ListaPrincipala'
    # context_object_name = 'DataActuala'
    template_name = 'base/paginaPrincipalaUser.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['ListaPrincipala'] = context['ListaPrincipala'].filter(workout__date=date.today())

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['ListaPrincipala'] = context['ListaPrincipala'].filter(oraInceput__icontains=search_input)

        context['search_input'] = search_input

        context['DataActuala'] = date.today()

        context['clasaRezervataLista'] = context['ListaPrincipala'].filter(listaParticipanti__icontains=self.request.user.username + " ;")

        try:
            context['clasaRezervata'] = context['clasaRezervataLista'][0]
        except:
            context['clasaRezervata'] = None

        return context

    def get(self, *args, **kwargs):
        if self.request.user.username == "Administrator":
            return redirect('paginaPrincipala')
        return super(PaginaUserView, self).get(*args, **kwargs)


class CustomWorkoutView(LoginRequiredMixin, DetailView):
    model = ClasaPrincipala
    context_object_name = 'ListaPrincipala'
    template_name = 'base/viewWorkout.html'
    succes_url = reverse_lazy('workoutPage')

    def reserveSpot(request, block_id):

        listaClase = ClasaPrincipala.objects.filter(workout__date=date.today())
        for clasa in listaClase:
            if(clasa.listaParticipanti is not None):
                if(request.user.username + " ;") in clasa.listaParticipanti:
                    return redirect("paginaPrincipalaUser")

        objectModel = ClasaPrincipala.objects.get(pk=block_id)

        if not objectModel.complete:  # and (not objectModel.listaParticipanti.contains(request.user.username + " ;"))):
            if objectModel.listaParticipanti is not None:
                if objectModel.listaParticipanti not in (request.user.username + " ;"):
                    objectModel.listaParticipanti += request.user.username + " ;"
                    objectModel.counterParticipanti += 1
            else:
                objectModel.listaParticipanti = request.user.username + " ;"
                objectModel.counterParticipanti = 1

        if objectModel.counterParticipanti == 5:
            objectModel.complete = True

        objectModel.save()
        return redirect("paginaPrincipalaUser")

    # functia pentru a da cancel la rezervare
    def cancelReservation(request, block_id):
        objectModel = ClasaPrincipala.objects.get(pk=block_id)

        if objectModel.listaParticipanti is None:
            return redirect("paginaPrincipalaUser")
        else:
            if (request.user.username + " ;") in objectModel.listaParticipanti:
                # fac stergerea din String. Scad counter, daca complete-ul in false (daca era false nu se schimba nimic,
                # daca era true, totul e bine pentru ca se schimba in false(nu mai avem clasa full)).
                if objectModel.counterParticipanti == 1:  # Daca am ajuns la un singur user, trebui sa punem lista si
                    # counter-ul pe None, nu pe "" si 0, pentru ca asa e functionalitatea noastra.
                    objectModel.listaParticipanti = None
                    objectModel.counterParticipanti = None
                else:  # altfel, inlocuim string-ul cu "", si scadem counter-ul cu 1.
                    objectModel.listaParticipanti = objectModel.listaParticipanti.replace(request.user.username + " ;","")
                    objectModel.counterParticipanti -= 1

                objectModel.complete = False
            else:  # altfel, daca user-ul nu are rezervare, il redirectionez (poate asta nu mai trebuie facuta daca
                # o sa afisez butonul doar daca am sau nu rezervare.)
                return redirect("paginaPrincipalaUser")

        objectModel.save()

        return redirect("paginaPrincipalaUser")

    def get(self, *args, **kwargs):
        if self.request.user.username == "Administrator":
            return redirect('paginaPrincipala')
        return super(CustomWorkoutView, self).get(*args, **kwargs)


class CustomAttendanceListView(LoginRequiredMixin, ListView):

    model = ClasaPrincipala
    context_object_name = 'ListaClasa'
    template_name = 'base/viewClassAttendanceList.html'
    succes_url = reverse_lazy('workoutPage')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['ListaClasa'] = context['ListaClasa'].filter(
            listaParticipanti__icontains=self.request.user.username + " ;")

        search_input1 = self.request.GET.get('Search-Area1') or ''
        # Conditie pentru search;
        if search_input1:
            context['ListaClasa'] = context['ListaClasa']. \
                filter(workout__date__icontains=search_input1)
        context['search_inputHtml1'] = search_input1;

        search_input2 = self.request.GET.get('Search-Area2') or ''
        # Conditie pentru search;
        if search_input2:
            context['ListaClasa'] = context['ListaClasa']. \
                filter(workout__title__icontains=search_input2)
        context['search_inputHtml2'] = search_input2;

        search_input3 = self.request.GET.get('Search-Area3') or ''
        # Conditie pentru search;
        if search_input3:
            context['ListaClasa'] = context['ListaClasa']. \
                filter(title__icontains=search_input3)
        context['search_inputHtml3'] = search_input3;

        return context

    def get(self, *args, **kwargs):
        if self.request.user.username == "Administrator":
            return redirect('paginaPrincipala')
        return super(CustomAttendanceListView, self).get(*args, **kwargs)

