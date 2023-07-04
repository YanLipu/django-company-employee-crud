from django.urls import path
from . import views



urlpatterns = [
    path('listar-usuarios', views.UserController.as_view()),
    path('login', views.LoginController.as_view()),
    path('logout', views.LogoutController.as_view()),
    path('list-companies', views.CompanyController.as_view()),
    path('company/<int:id>', views.GetCompanyIdController.as_view()),
    path('create-company', views.CompanyController.as_view()),
    path('edit-company/<int:id>', views.CompanyController.as_view()),
    path('delete-company/<int:id>', views.CompanyController.as_view()),
    path('list-employes', views.EmployeController.as_view()),
    path('employee/<int:id>', views.GetEmployeIdController.as_view()),
    path('create-employe', views.EmployeController.as_view()),
    path('edit-employe/<int:id>', views.EmployeController.as_view()),
    path('delete-employe/<int:id>', views.EmployeController.as_view()),
    # path('listar-grupos', views.GrupoController.as_view()),
    # path('criar-grupo', views.GrupoController.as_view()),
    # path('editar-grupo/<int:id>', views.GrupoController.as_view()),
    # path('excluir-grupo/<int:id>', views.GrupoController.as_view()),
    # path('criar-usuario', views.UsuarioController.as_view()),
    # path('editar-usuario/<int:id>', views.UsuarioController.as_view()),
    # path('excluir-usuario/<int:id>', views.UsuarioController.as_view()),
]