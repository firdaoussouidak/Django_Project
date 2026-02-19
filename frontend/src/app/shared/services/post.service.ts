import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface PostData {
  id: number;
  title: string;
  accroche: string;
  citation: string;
  auteur_signature: string;
  handle: string;
  content: string;
  style: string;
  theme: string;
  bg: string;
  image?: string;
  author_id: number;
  author_username: string;
  date: string;
  comments_count: number; 
}

@Injectable({ providedIn: 'root' })
export class PostService {
  private apiUrl = 'http://localhost:8000/api/post'; 
  constructor(private http: HttpClient) {}

  createPost(formData: FormData): Observable<any> {
    return this.http.post(`${this.apiUrl}/create/`, formData);
  }

  getPosts(): Observable<PostData[]> {
    return this.http.get<PostData[]>(`${this.apiUrl}/list/`);
  }

  getMyPosts(): Observable<PostData[]> {
    return this.http.get<PostData[]>(`${this.apiUrl}/my-posts/`);
  }

  deletePost(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/delete/${id}/`);
  }

  updatePost(id: number, formData: FormData): Observable<any> {
    return this.http.put(`${this.apiUrl}/update/${id}/`, formData);
  }
}