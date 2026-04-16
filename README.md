# TKiK-skaner

### Specyfikacja Tokenów

Skaner dzieli kod źródłowy na następujące jednostki leksykalne (tokeny):

| Typ Tokena | Opis / Wartość | Przykład |
| :--- | :--- | :--- |
| **ID** | Identyfikator (nazwa zmiennej) | `x`, `wynik`, `temp1` |
| **KEYWORD** | Słowo kluczowe zarezerwowane przez język | `if`, `then`, `else`, `end` |
| **NUMBER** | Liczba całkowita (integer) | `2`, `76`, `1024` |
| **PLUS** | Operator dodawania | `+` |
| **MINUS** | Operator odejmowania | `-` |
| **MUL** | Operator mnożenia | `*` |
| **DIV** | Operator dzielenia | `/` |
| **ASSIGN** | Operator przypisania | `=` |
| **LPAREN** | Lewy nawias | `(` |
| **RPAREN** | Prawy nawias | `)` |
| **EOF** | Koniec strumienia danych (End Of File) | *brak* |
| **ERROR** | Nieoczekiwany znak lub błąd leksykalny | `@`, `$` |

---

### Zasady działania skanera
* **Pominięcia:** Skaner automatycznie ignoruje białe znaki (spacje, tabulacje).
* **Case Insensitivity:** Słowa kluczowe są rozpoznawane bez względu na wielkość liter (dzięki `value.lower()`).
* **Priorytetyzacja:** Każdy ciąg alfanumeryczny zaczynający się od litery jest najpierw sprawdzany pod kątem bycia słowem kluczowym; jeśli nim nie jest, zostaje uznany za identyfikator (`ID`).
