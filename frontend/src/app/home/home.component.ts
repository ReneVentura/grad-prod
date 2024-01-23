import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  selectedFile?: File;
  uploaded = false;
  data: Record<string, string> = {};
  res: any
    constructor(private http: HttpClient) {}

  onFileSelected(event: Event): void {
    // Hacemos un casting del tipo de 'event.target' a 'HTMLInputElement'
    const input = event.target as HTMLInputElement;
  
    // Ahora podemos acceder a 'files' de manera segura, asegurándonos primero de que no es nulo
    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
    }
  }
  uploadFile(event:Event): void {
    event.preventDefault();
    
    // Verifica si se ha seleccionado un archivo
    if (this.selectedFile) {
      const formData = new FormData();
      formData.append('file', this.selectedFile, this.selectedFile.name);
      const dataJsonString = JSON.stringify(this.data);
      formData.append('data', dataJsonString);
      this.http.post('http://localhost:5000/upload', formData)
        .subscribe(response => {
          this.uploaded = true;
          console.log(response)
          this.res = response
        });
    } else {
      // Maneja el caso en que no se haya seleccionado un archivo
      console.error('No file selected');
    }
  }

  onRadioSelected(event: Event, radioGroupName: string): void {
    const inputElement = event.target as HTMLInputElement;
    this.data[radioGroupName] = inputElement.value;

  }
  onNumericInput(event: Event): void {
    const inputElement = event.target as HTMLInputElement;
    this.data['longitud'] = inputElement.value;
  }

  sendData(){
    console.log(this.data)
  }
  
}
