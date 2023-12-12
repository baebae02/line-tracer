// 라즈베리파이 코드
#ifdef RaspberryPi 

//include system librarys
#include <stdio.h> //for printf
#include <stdint.h> //uint8_t definitions
#include <stdlib.h> //for exit(int);
#include <string.h> //for errno
#include <errno.h> //error output

//wiring Pi
#include <wiringPi.h>
#include <wiringSerial.h>

// Find Serial device on Raspberry with ~ls /dev/tty*
// 연결된 장치 찾는 방법은 라즈베리파이 터미널 창에서
// dmesg|tail을 통해서  USB 장치 확인 
// 만약 끝부분에 나오지 않는다면 전체를 보기위해
// dmesg > test.txt 라는 명령어로 텍스트 파일에 저장해서 본다.
// ARDUINO_UNO "/dev/ttyACM0"
// FTDI_PROGRAMMER "/dev/ttyUSB0"
// HARDWARE_UART "/dev/ttyAMA0"
char device[] = "/dev/ttyACM0";
// filedescriptor
int fd;
unsigned long baud = 9600; //보드 레이트

unsigned long time = 0;

//prototypes
void loop(void);
void setup(void);


// 초기 파일 디스크립터 설정
// wiringPi 설정
void setup() {
	printf("%s \n", "Raspberry Startup!");
	fflush(stdout);

	//get filedescriptor
	if ((fd = serialOpen(device, baud)) < 0) {
		fprintf(stderr, "Unable to open serial device: %s\n", strerror(errno));
		exit(1); //error
	}

	//setup GPIO in wiringPi mode
	if (wiringPiSetup() == -1) {
		fprintf(stdout, "Unable to start wiringPi: %s\n", strerror(errno));
		exit(1); //error
	}
}

char putChar[] = "L"; // 아두이노로 보낼 프로토콜// 개행 문자를 넣지 않으면 아두이노 측에서 보낼 때 개행을 추가해줘야함.
int chk = 1;
int i;
int j;
char getChar[] = ""; // 아두이노에서 Echo로 보낼 문자(1Byte)를 저장해둘 버퍼

void loop()
{
	// send 1byte
	if (putChar[i] != '\0') {
		serialPutchar(fd, putChar[i++]);
		delay(50); // 딜레이가 없으면 잘 나오다가 hhhhhhhhheeeeeeeeeeeelllllllllllllllllllllooooooooooo 이런식으로 나오게 됨.
	}
	else
	{
		i = 0;
	}

	// read signal
	// serialDataAvail 함수의 리턴 값은 fd 에서 읽을 수 있는 바이트.
	if (serialDataAvail(fd))
	{
		// serialGets(fd)라는 명령어도 있지만 잘 안돼서 한 바이트씩 받기 위해 반복문을 이용함
		char readData = serialGetchar(fd);
		delay(50);
		getChar[j++] = readData; // 아두이노에서 읽은 데이터를 버퍼에 저장
		if (readData == '\n')  // hello\n을 보내므로 끝 문자인 \n이 들어오면 버퍼 초기화 및 인자 초기화
		{
			//printf("getChar: %s",getChar);
			//printf("put: %d get: %d\n", strlen(putChar), strlen(getChar));
			printf("%d\n", strcmp(putChar, getChar));
			if (!strcmp(putChar, getChar))
			{
				serialPutchar(fd, 'Y');
				delay(50);
				char readAgainData = serialGetchar(fd);
				delay(50);
				printf("%c\n", readAgainData);
				chk = 0;
				return;
			}
			else
			{
				serialPutchar(fd, 'N');
				delay(50);
				char readAgainData = serialGetchar(fd);
				delay(50);
				printf("%c\n", readAgainData);
				if (readAgainData == 'N')
				{
					i = 0; j = 0;
					memset(getChar, '\0', j);
					return;
				}
			}

			memset(getChar, '\0', j);
			j = 0;
		}
	}
}

// main function for normal c++ programs on Raspberry
int main() {

	setup();
	while (chk)
	{
		loop();
	}
	serialClose(fd);

	printf("finish....................\n");
	return 0;
}

#endif //#ifdef RaspberryPi


