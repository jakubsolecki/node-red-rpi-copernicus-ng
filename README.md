# node-red-rpi-copernicus-ng

## Inicjalizacja

Zanim zacznie sie korzystać z pinów trzeba je zainicjalizować wysyłając odpowiednie JSONy na 

```python
{topic}/{device_id}/init
```


Jak na razie obsługiwane urządzenia to
<ul>
<li>DigitalOutput - np LED, albo Buzzer</li>
<li>DigitalInput - np Button</li>
</ul>


Inicjalizacja LED na pinie 21
```JavaScript
    {
	"init": true,
	"pin": 21,
	"type": "DigitalOutput"
    }
```

Inicjalizacja Buttona na pinie 11
```JavaScript
    {
	"init": true,
	"pin": 11,
	"type": "DigitalInput"
    }
```

## Otrzymywanie sygnałów

W momencie w którym jeden z outputów wyśle sygnał (np ktoś wciśnie ZAINICJALIZOWANY button) zostanie wysłana wiadomość na

```Python
{topic}/{device_id}/output
```

Przykładowa wiadomość po przyciśnięciu Buttona


```javascript
    {
        "pin": 11, 
        "state": 0
    }
```

Button wysyła jak zmieni się stan (tzn jak zostanie wciśnięty lub odciśnięty)


## Wysyłanie sygnałów

Możemy również wysyłać sygnały do płytki wpływając na DigitalOutputy

```
{topic}/{device_id}/input
```

Na przykład

```javascript
    {
	"init": false,
	"pin": 22,
	"state": 1
    }
```
Powyższe włączy leda