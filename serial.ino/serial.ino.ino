#include <AFMotor.h>
AF_DCMotor motor1(2); 
AF_DCMotor motor2(3);
int speed = 255;

// initial command
int command = 0;

// main.py로부터 받아온 direction이 유효한 값인지 확인하는 함수
bool is_valid_direction(char direction)
{
  switch (direction)
  {
    case 'T': case 'l': case 'L': case 'r': case 'R': case 'B':
      return true;
  }

  return false;
}

void setup()
{
  // turn on motor 
  motor1.setSpeed(200); 
  motor2.setSpeed(200);
  motor1.run(RELEASE);
  motor2.run(RELEASE); 
  Serial.begin(9600);

  while (!Serial);

  Serial.println("Mars 2020");
}

void loop()
{
  if (Serial.available())
  {
    char direction;

    do
    {
      direction = Serial.read();
    }
    while (!is_valid_direction(direction));

    switch (direction)
    {
      //forward
      case 'T':
        motor1.run(FORWARD);
        motor2.run(FORWARD);
        break;

      //left
      case 'l' :
        motor2.setSpeed(50);
        motor1.setSpeed(speed);
        break;

      //strong left
      case 'L':
        motor2.setSpeed(200);
        motor1.setSpeed(speed);
        break;

      //right
      case 'r':
        motor1.setSpeed(50);
        motor2.setSpeed(speed);
        break;

      //strong right
      case 'R':
        motor1.setSpeed(200);
        motor2.setSpeed(speed);
        break;

      //back
      case 'B' :
        motor1.run(BACKWARD);
        motor2.run(BACKWARD);
        break;
    }
    if(direction == 'R' || direction == 'L'){
      delay(20);
    }
    if(direction == 'B'){
      delay(100);
    }
    else{
      delay(60);
    }
    motor1.setSpeed(0);
    motor2.setSpeed(0);
    //main.py에게 ACK 전송
    Serial.write("ACK\n");
    delay(50);
  }
}