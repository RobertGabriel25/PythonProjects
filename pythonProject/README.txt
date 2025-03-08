******************************************************************************************************************************************************************************
******************************************************************************************************************************************************************************
******************************************************************************************************************************************************************************
******************************************************************************************************************************************************************************
******************************************************************************************************************************************************************************
Pentru a rula trebuie instalate tkinter si threading, apoi incarcat fisierul in IDE-ul
utilizatorului de unde se ruleaza fisierul main.py.


Referinte folosite:
https://www.chat.openai.com pentru a incerca fara succes de a implementa backgroundul ca
background_image.jpg

https://www.youtube.com/@NeuralNine
https://www.youtube.com/watch?v=quBb--IJPPc&ab_channel=NeuralNine




	Descriere a Modului de Funcționare:

Programul Speed Typing Game vă permite să vă îmbunătățiți abilitățile de tastare într-un mod interactiv și distractiv.
 Acesta generează fraze aleatoare pe care utilizatorul trebuie să le introducă cât mai rapid și fără erori posibile. 
Iată cum să utilizați programul:

Instalare și Configurare:

Asigurați-vă că aveți Python instalat pe computer.
Folosiți comanda pip install tk pentru a instala Tkinter, dacă nu este deja instalat.
Descărcare și Lansare:

Execuție:


Interfața grafică a jocului va apărea cu o frază aleatoare.
Introduceți fraza în câmpul de tastare cât mai rapid și fără erori posibile.
Funcționalități:

Apăsați orice tasta pentru a începe jocul, de preferat primul caracter al frazei cerute.
Corectați eventualele erori prin tastarea corectă.
După terminarea corectă a unei fraze, apăsați butonul "Reset" pentru o nouă provocare.
Rezultate și Statistici:

Viteza de tastare și statistici vor fi afișate în timpul jocului.
Programul calculează caracterele pe secundă și pe minut.
Închidere:

Închideți fereastra jocului sau apăsați Ctrl+C în terminal pentru a închide scriptul.
Atenție: Pentru o experiență optimă, asigurați-vă că aveți o conexiune la internet pentru a descărca imaginile de 
fundal și aveți permisiunile necesare pentru a instala pachete Python folosind pip.


Modul de Rulare al Programului:

Inițierea Aplicației:

Aplicația începe prin crearea unei instanțe a clasei Viteza.
Se creează fereastra principală utilizând Tk(), se încarcă frazele din fișierul "texts.txt",
iar apoi se inițializează interfața grafică a jocului.
Interfața Grafică:


Widget-urile precum etichetele, câmpul de introducere și butoanele sunt create și plasate în cadrul ferestrei principale.
Generarea de Fraze Aleatoare:

O frază aleatoare este selectată din lista de fraze posibile folosind random.choice.
Evenimentul de Tastare:

Atunci când utilizatorul apasă o tastă (<KeyPress>), este apelată funcția start.
Dacă jocul nu a fost terminat, verifică dacă tastatura nu este utilizată pentru taste speciale și, 
în caz afirmativ, începe jocul pornind firul de execuție time_thread.

Firul de Execuție pentru Măsurarea Timpului:

Folosind un fir de execuție separat (threading.Thread), programul măsoară timpul în fundal.
Actualizările rapide ale etichetei de viteză sunt realizate la fiecare 0.1 secunde.
Resetează Jocul:

Dacă utilizatorul apasă butonul "Reset", jocul se resetează la o nouă frază aleatoare.
Afișarea Vitezei și Rezultatelor:

Viteza de tastare este calculată și afișată în timp real în eticheta corespunzătoare.
Terminarea Jocului:

Jocul se termină atunci când utilizatorul introduce corect fraza sau când butonul "Reset" este apăsat.
Culorile textului se schimbă în funcție de corectitudine (roșu pentru erori, verde pentru succes).
Închiderea Programului:

Programul poate fi închis prin închiderea ferestrei sau prin apăsarea Ctrl+C în terminal.
Funcții Importante:

start: Gestionează începerea jocului și pornirea firului de execuție.
time_thread: Măsoară timpul și actualizează viteză în fundal.
reset: Resetează jocul la o stare inițială.
mainloop: Lansează bucla principală de evenimente Tkinter.

******************************************************************************************************************************************************************************
******************************************************************************************************************************************************************************
******************************************************************************************************************************************************************************
******************************************************************************************************************************************************************************
******************************************************************************************************************************************************************************