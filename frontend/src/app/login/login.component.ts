import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  imports: [FormsModule, CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  email: string = '';
  password: string = '';
  rememberMe: boolean = false;

  constructor(private router: Router) {}

  onSubmit(): void {
    console.log('Login submitted:', {
      email: this.email,
      password: this.password,
      rememberMe: this.rememberMe
    });
  }

  onForgotPassword(event: Event): void {
    event.preventDefault();
    console.log('Forgot password clicked');
  }

  onLogin(event: Event): void {
    event.preventDefault();
    console.log('Login clicked');
    this.router.navigate(['/posts']);
  }

  onRegister(event: Event): void {
    event.preventDefault();
    console.log('Register clicked');
    this.router.navigate(['/signup']);
  }
}