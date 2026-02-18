import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { AuthService } from '../../shared/services/auth.service';

@Component({
  selector: 'app-signup',
  imports: [FormsModule, CommonModule],
  templateUrl: './signup.component.html',
  styleUrl: './signup.component.css'
})
export class SignupComponent {
  username: string = '';
  first_name: string = '';
  last_name: string = '';
  email: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit(): void {
    this.errorMessage = '';

    this.authService.signup({
      username: this.username,
      first_name: this.first_name,
      last_name: this.last_name,
      email: this.email,
      password: this.password
    }).subscribe({
      next: (response) => {
        console.log('Inscription réussie', response);
        // Rediriger vers la page de connexion
        this.router.navigate(['/login']);
      },
      error: (err) => {
        console.error('Erreur inscription', err);
        if (err.status === 400) {
          // Gestion basique des erreurs de validation
          if (err.error?.username) {
            this.errorMessage = 'Nom d\'utilisateur déjà pris.';
          } else if (err.error?.email) {
            this.errorMessage = 'Email déjà utilisé.';
          } else {
            this.errorMessage = 'Données invalides. Vérifiez le formulaire.';
          }
        } else if (err.status === 0) {
          this.errorMessage = 'Serveur inaccessible.';
        } else {
          this.errorMessage = 'Une erreur est survenue.';
        }
      }
    });
  }

  onLogin(event: Event): void {
    event.preventDefault();
    this.router.navigate(['/login']);
  }
}