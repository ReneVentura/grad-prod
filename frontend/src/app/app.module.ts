import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module'; // Asegúrate de importar AppRoutingModule
import { HomeComponent } from './home/home.component';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
@NgModule({
  declarations: [
    HomeComponent,
    AppComponent
    // otros componentes...
  ],
  imports: [
    BrowserModule,
    AppRoutingModule, // Asegúrate de incluir AppRoutingModule aquí
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
