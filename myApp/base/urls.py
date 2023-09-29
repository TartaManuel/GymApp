from django.urls import path
from . import views
from .views import PaginaPrincipalaView, CustomDetailView1, CustomCreateView1, CustomUpdateView1, CustomDeleteView1,CustomCreateView2, CustomUpdateView2, CustomDeleteView2, CustomLoginView, CustomRegisterView, PaginaWorkoutView
from .views import PaginaUserView, CustomWorkoutView, CustomAttendanceListView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', PaginaPrincipalaView.as_view(), name='paginaPrincipala'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    # se va uita dupa acest primary key, care e int in modelul TestClasa
    path('afisare/<int:pk>/', CustomDetailView1.as_view(), name='afisare'),
    path('creare/', CustomCreateView1.as_view(), name='creare'),
    path('update/<int:pk>/', CustomUpdateView1.as_view(), name='update'),
    path('delete/<int:pk>/', CustomDeleteView1.as_view(), name='delete'),
    path('workoutPage/', PaginaWorkoutView.as_view(), name='workoutPage'),
    path('creareWorkout/', CustomCreateView2.as_view(), name='creareWorkout'),
    path('updateWorkout/<int:pk>/', CustomUpdateView2.as_view(), name='updateWorkout'),
    path('deleteWorkout/<int:pk>/', CustomDeleteView2.as_view(), name='deleteWorkout'),
    path('user/', PaginaUserView.as_view(), name='paginaPrincipalaUser'),
    path('viewWorkout/<int:pk>/', CustomWorkoutView.as_view(), name='viewWorkout'),

    path(r'^reserveSpot/(?P<block_id>\d+)/$', CustomWorkoutView.reserveSpot, name='reserveSpot'),
    path('viewClassAttendanceList/', CustomAttendanceListView.as_view(), name='viewClassAttendanceList'),
    path(r'^cancelReservation/(?P<block_id>\d+)/$', CustomWorkoutView.cancelReservation, name='cancelReservation'),
]
