//Подключение библиотеки для работы с DHT22 
#include "DHT.h"
//Объявление переменных и связывание названий с реальными выходами Atmega328P 
#define PIN_RELAY1 5
#define PIN_RELAY2 6
#define PIN_RELAY3 7
#define DHTPIN A0 
//Инициализируем датчик
DHT dht (DHTPIN, DHT22);

void setup () {
  pinMode(PIN_RELAY1, OUTPUT); //Объявляем разъем реле1 как выход
  pinMode(PIN_RELAY2, OUTPUT); //Объявляем разъем реле2 как выход
  pinMode(PIN_RELAY3, OUTPUT); //Объявляем разъем реле3 как выход
  digitalWrite(PIN_RELAY1, LOW); //Выключаем реле - посылаем высокий сигнал
  digitalWrite(PIN_RELAY2, LOW); //Выключаем реле - посылаем высокий сигнал
  digitalWrite(PIN_RELAY3, LOW); //Выключаем реле - посылаем высокий сигнал
  Serial.begin(9600);
  dht.begin();
}

void loop () {
  delay (2000); //2 секунды задержки
  float h = dht.readHumidity(); //Измеряем влажность
  float t = dht.readTemperature(); //Измеряем температуру
  
//Проверка. Если не удается считать показания, выводится «Ошибка считывания», и программа завершает работу
  if (isnan(h) || isnan(t)) {  
    Serial.println("Ошибка считывания");
    return;
  }
  //Если влажность НИЖЕ 93% включаем РЕЛЕ1 (управление увлажнителем воздуха)
  if (h < 93){
    digitalWrite(PIN_RELAY1, HIGH); 
  }
  else {
    digitalWrite(PIN_RELAY1, LOW);
  }

  // Если температура НИЖЕ 2°C включаем РЕЛЕ2 (нагревание воздуха)
  if (t < 2){
    digitalWrite(PIN_RELAY2, HIGH);
  }
  else {
    digitalWrite(PIN_RELAY2, LOW);
  }

  // Если температура ВЫШЕ 2°C включаем РЕЛЕ3 (охлаждение воздуха)
  if (t > 2){
    digitalWrite(PIN_RELAY3, HIGH);
  }
  else {
    digitalWrite(PIN_RELAY3, LOW);
  }

  //Отправка данных через TX вывод Atmega328P
  Serial.print("h:");
  Serial.print(h);
  Serial.print("t:");
  Serial.print(t);
  Serial.println();
}
