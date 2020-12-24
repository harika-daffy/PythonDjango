import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';

interface myData{
  success:boolean,
  message:string
}
interface registerResponse{
  success:boolean
  message:string
}

@Injectable()
export class AuthService {
  private loggedInStatus=false;
  
  setLoggedIn(value: boolean){
    this.loggedInStatus=value
  }
  get isLoggedIn(){
    return this.loggedInStatus
  }
  constructor(private http: HttpClient ) {
    const headers= new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    //this.contents = '';
   }

  getUserDetails(username,password){
    return this.http.post<myData>('http://localhost:8001/api/login',{
      username,password
    })
  }
  registerUser(username,password){
    return this.http.post<registerResponse>('http://localhost:8001/api/register',{
      username,
      password
    })
  }
  
}
