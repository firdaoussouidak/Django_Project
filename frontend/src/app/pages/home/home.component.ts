import { Component, OnInit, OnDestroy } from '@angular/core';
import { CommonModule, NgFor, NgIf } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';

export interface Post {
  id: number;
  style: 'minimal' | 'editorial' | 'citation' | 'portrait';
  frameStyle: 'ps7' | 'ps9' | 'ps14' | 'ps11' | 'ps16' | 'ps6';
  word?: string;
  title?: string;
  body?: string;
  quote?: string;
  author?: string;
  handle?: string;
  image?: string;
  authorName: string;
  authorInitials: string;
  authorColor: string;
  likes: number;
  liked: boolean;
  hovered: boolean;
  comments: number;
}

export interface Creator {
  name: string;
  initials: string;
  handle: string;
  color: string;
  followed: boolean;
}

export interface Activity {
  icon: string;
  text: string;
  time: string;
}

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, FormsModule, NgFor, NgIf, RouterLink],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit, OnDestroy {
  userInitials = 'EJ';
  stats = { posts: 24, followers: '1.2k', likes: 348 };

  activeNav = 'feed';
  notifCount = 3;

  activeFilter: 'all' | 'minimal' | 'editorial' | 'citation' | 'portrait' = 'all';

  activeSort = 'recent';
  sortOptions = [
    { label: 'Récents',      value: 'recent' },
    { label: 'Populaires',   value: 'popular' },
    { label: 'Abonnements',  value: 'followed' },
  ];

  searchQuery = '';
  private searchTimer: any;

  toastMessage = '';
  toastVisible = false;
  private toastTimer: any;

  posts: Post[] = [
    {
      id: 1,
      style: 'minimal',
      frameStyle: 'ps7',
      word: 'Motivation',
      title: 'Big ideas have small beginnings',
      body: 'Nunc lacinia lacus tortor, vel consectetur neque condimentum vel. Vivamus facilisis arcu vel amet lorem.',
      handle: '@ellejames',
      authorName: 'Elle James',
      authorInitials: 'EJ',
      authorColor: '#5c1a1a',
      likes: 24,
      liked: false,
      hovered: false,
      comments: 8,
    },
    {
      id: 2,
      style: 'editorial',
      frameStyle: 'ps9',
      word: 'Lifestyle',
      title: 'Vers de nouveaux horizons',
      body: 'Chaque matin est une nouvelle page blanche.',
      handle: '@sophiemrt',
      image: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&q=80',
      authorName: 'Sophie M.',
      authorInitials: 'SM',
      authorColor: '#7a3520',
      likes: 61,
      liked: false,
      hovered: false,
      comments: 8,
    },
    {
      id: 3,
      style: 'citation',
      frameStyle: 'ps14',
      quote: 'What if today was the day you have been waiting for? Act now, live fully.',
      authorName: 'Léa B.',
      authorInitials: 'LB',
      authorColor: '#0d1f3c',
      likes: 103,
      liked: false,
      hovered: false,
      comments: 8,
    },
    {
      id: 4,
      style: 'portrait',
      frameStyle: 'ps11',
      title: "L'art de bien vivre chaque instant",
      body: 'Cultivez la gratitude et la beauté dans les petites choses.',
      handle: '@marieclaire',
      image: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&q=80',
      authorName: 'Marie Claire',
      authorInitials: 'MC',
      authorColor: '#7a2e4a',
      likes: 88,
      liked: false,
      hovered: false,
      comments: 8,
    },
    {
      id: 5,
      style: 'citation',
      frameStyle: 'ps16',
      quote: "La nature est la plus grande des œuvres d'art.",
      author: '— Victor Hugo',
      image: 'https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=400&q=80',
      authorName: 'Nora F.',
      authorInitials: 'NF',
      authorColor: '#1a3320',
      likes: 47,
      liked: false,
      hovered: false,
      comments: 8,
    },
    {
      id: 6,
      style: 'editorial',
      frameStyle: 'ps6',
      title: 'Savoir ralentir pour mieux avancer',
      body: "Le repos est une forme de courage. Accordez-vous ce luxe précieux chaque jour.",
      image: 'https://images.unsplash.com/photo-1520962880247-cfaf541c8724?w=400&q=80',
      authorName: 'Axel R.',
      authorInitials: 'AR',
      authorColor: '#3a3a18',
      likes: 35,
      liked: false,
      hovered: false,
      comments: 8,
    },
  ];

  get filteredPosts(): Post[] {
    let result = [...this.posts];
    if (this.activeFilter !== 'all') {
      result = result.filter(p => p.style === this.activeFilter);
    }
    if (this.searchQuery.trim().length > 1) {
      const q = this.searchQuery.toLowerCase();
      result = result.filter(p =>
        (p.title?.toLowerCase().includes(q)) ||
        (p.body?.toLowerCase().includes(q)) ||
        (p.quote?.toLowerCase().includes(q)) ||
        (p.authorName.toLowerCase().includes(q)) ||
        (p.handle?.toLowerCase().includes(q))
      );
    }
    if (this.activeSort === 'popular') {
      result = [...result].sort((a, b) => b.likes - a.likes);
    }
    return result;
  }

  trendingTags = [
    '#motivation', '#art', '#lifestyle', '#citation',
    '#bienêtre', '#mode', '#voyage', '#nature'
  ];

  suggestedCreators: Creator[] = [
    { name: 'Sophie M.',   initials: 'SM', handle: '@sophiemrt',   color: '#7a3520', followed: false },
    { name: 'Léa B.',      initials: 'LB', handle: '@leab_writes', color: '#0d1f3c', followed: false },
    { name: 'Marie Claire',initials: 'MC', handle: '@marieclaire', color: '#7a2e4a', followed: false },
  ];

  /* ── Activity ── */
  recentActivity: Activity[] = [
    { icon: '♡', text: '<strong>Sophie M.</strong> a aimé votre post',         time: 'Il y a 5 min' },
    { icon: '⟳', text: '<strong>Léa B.</strong> a partagé votre citation',     time: 'Il y a 23 min' },
    { icon: '✦', text: '<strong>Axel R.</strong> a commencé à vous suivre',    time: 'Il y a 1h' },
  ];

  constructor(private router: Router) {}

  ngOnInit(): void {}

  ngOnDestroy(): void {
    clearTimeout(this.toastTimer);
    clearTimeout(this.searchTimer);
  }

  setNav(nav: string): void {
    this.activeNav = nav;
    this.showToast(nav === 'feed' ? 'Fil d\'actualité' : nav);
  }

  goToProfile(): void {
    this.showToast('Profil');
    // this.router.navigate(['/profile']);
  }

  goToCreate(): void {
    this.showToast('Créer un post');
    this.router.navigate(['/posts']);
  }

  goToSettings(): void {
    this.showToast('Paramètres');
    // this.router.navigate(['/settings']);
  }

  logout(): void {
    this.showToast('Déconnexion…');
    this.router.navigate(['/login']);
  }

  filterStyle(style: typeof this.activeFilter): void {
    this.activeFilter = style;
    this.showToast(style === 'all' ? 'Tous les styles' : 'Filtre : ' + style);
  }

  setSort(value: string): void {
    this.activeSort = value;
    const label = this.sortOptions.find(s => s.value === value)?.label ?? value;
    this.showToast(label);
  }

  handleSearch(): void {
    clearTimeout(this.searchTimer);
    if (this.searchQuery.trim().length > 2) {
      this.searchTimer = setTimeout(() => {
        this.showToast('Recherche : ' + this.searchQuery.trim());
      }, 600);
    }
  }

  searchTag(tag: string): void {
    this.searchQuery = tag;
    this.showToast('Tendance : ' + tag);
  }

  toggleLike(post: Post): void {
    post.liked = !post.liked;
    post.likes += post.liked ? 1 : -1;
  }

  commentPost(post: Post): void {
    this.showToast('Commentaires du post #' + post.id);
    // this.router.navigate(['/post', post.id, 'comments']);
  }

  viewPost(post: Post): void {
    this.showToast('Voir le post #' + post.id);
    // this.router.navigate(['/post', post.id]);
  }

  editPost(post: Post): void {
    this.showToast('Éditer le post #' + post.id);
    // this.router.navigate(['/edit', post.id]);
  }

  toggleFollow(creator: Creator): void {
    creator.followed = !creator.followed;
    this.showToast(creator.followed ? 'Abonné à ' + creator.name : 'Abonnement annulé');
  }

  showToast(message: string): void {
    clearTimeout(this.toastTimer);
    this.toastMessage = message;
    this.toastVisible = true;
    this.toastTimer = setTimeout(() => { this.toastVisible = false; }, 1800);
  }
}