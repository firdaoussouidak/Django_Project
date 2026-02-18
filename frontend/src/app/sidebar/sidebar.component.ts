import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './sidebar.component.html',
  styleUrl: './sidebar.component.css'
})
export class SidebarComponent {
  onSearch(event: Event): void {
    event.preventDefault();
    const form = event.target as HTMLFormElement;
    const input = form.querySelector('.search-input') as HTMLInputElement;
    const query = input.value.trim();
    if (query) {
      console.log('Recherche :', query);
      // Ici vous pouvez émettre un événement ou naviguer vers une page de résultats
    }
  }
}
