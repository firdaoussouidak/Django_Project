import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { AuthService } from '../../shared/services/auth.service';

@Component({
  selector: 'app-login',
  imports: [FormsModule, CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  username: string = '';        
  password: string = '';
  errorMessage: string = ''; 

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit(): void {
    this.errorMessage = ''; 

    this.authService.login({
      username: this.username,
      password: this.password
    }).subscribe({
      next: (response) => {
        console.log('Connexion réussie', response);
        this.router.navigate(['/home']);
      },
      error: (err) => {
        console.error('Erreur complète :', err);
        if (err.status === 0) {
          this.errorMessage = 'Serveur inaccessible (CORS ?). Vérifiez que le backend est lancé.';
        } else if (err.status === 400) {
          this.errorMessage = 'Identifiants incorrects.';
        } else if (err.status === 404) {
          this.errorMessage = 'URL API introuvable.';
        } else {
          this.errorMessage = `Erreur ${err.status} : ${err.statusText}`;
        }
      }
    });
  }

  onForgotPassword(event: Event): void {
    event.preventDefault();
    this.router.navigate(['/forgot-password']);
  }

  onLogin(event: Event): void {
    event.preventDefault(); 
    this.onSubmit();
  }

  onRegister(event: Event): void {
    event.preventDefault();
    this.router.navigate(['/signup']);
  }
  
}