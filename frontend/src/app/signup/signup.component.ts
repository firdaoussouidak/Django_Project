import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

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

  constructor(private router: Router) {}

  onSubmit(): void {
    console.log('SignUp submitted:', {
      username: this.username,
      first_name: this.first_name,
      last_name: this.last_name,
      email: this.email,
      password: this.password
    });
  }

  onLogin(event: Event): void {
    event.preventDefault();
    console.log('Login clicked');
    this.router.navigate(['/login']);
  }
}