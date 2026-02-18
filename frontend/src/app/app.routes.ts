import { Routes } from '@angular/router';

export const routes: Routes = [
{
        path:'',
        redirectTo:'login',
        pathMatch:'full'
    },
    {
        path: 'login',
        loadComponent: () => import('./login/login.component').then(m => m.LoginComponent)
    },
    {
        path: 'signup',
        loadComponent: () => import('./signup/signup.component').then(m => m.SignupComponent)
    },
    {
        path: 'posts',
        loadComponent: () => import('./posts/posts.component').then(m => m.PostsComponent)
    },
    {
        path: 'sidebar',
        loadComponent: () => import('./sidebar/sidebar.component').then(m => m.SidebarComponent)
    }
];