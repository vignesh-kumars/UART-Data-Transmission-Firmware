#define E2END 1023 
void setup() {
  Serial.begin(2400);
}

void data_write_to_eprom(int w_r_address, byte w_r_values) {
  while (EECR & (1 << EEPE)) {} 
  EEAR = w_r_address; 
  EEDR = w_r_values;
  EECR |= (1 << EEMPE); 
  EECR |= (1 << EEPE); 
}

byte data_read_to_eprom(int w_r_address) {
  while (EECR & (1 << EEPE)) {} 
  EEAR = w_r_address; 
  EECR |= (1 << EERE); 
  return EEDR; 
}

void loop() {
  if (Serial.available() > 0) {
    String info_received = Serial.readStringUntil('\n'); 
    int Length_of_string = info_received.length();
    
    int memory_address = 0; 
    for (int i = 0; i <Length_of_string; i++) {
      data_write_to_eprom(memory_address + i,info_received[i]);
    }
    Serial.println(info_received);

    delay(100);
  }

  
  if (Serial.available() > 0) {
    int startAddress = Serial.parseInt();
    int strLength = Serial.parseInt();
    
    
    String storedData = "";
    for (int i = 0; i < strLength; i++) {
      char ch = data_read_to_eprom(startAddress + i);
      storedData += ch;
    }
    
    Serial.print(storedData);
    

    delay(100);
  }
}