import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface PostData {
  title: string;
  accroche: string;
  citation: string;
  auteur_signature: string;
  handle: string;
  content: string;
  style: string;
  theme: string;
  bg: string;
}

@Injectable({ providedIn: 'root' })
export class PostService {
  private apiUrl = 'http://localhost:8000/api/post'; 
  constructor(private http: HttpClient) {}

  createPost(formData: FormData): Observable<any> {
    return this.http.post(`${this.apiUrl}/create/`, formData);
  }
}