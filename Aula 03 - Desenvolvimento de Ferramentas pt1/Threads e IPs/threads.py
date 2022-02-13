from threading import Thread
import time

def car(id, velocity):
  position = 0
  while position <= 100:
    print(f"Carro {id}: {position}")
    position += velocity
    time.sleep(0.5)

if __name__ == "__main__":
  t_car_1 = Thread(target=car, args=[1, 1])
  t_car_2 = Thread(target=car, args=[2, 1.5])

  t_car_1.start()
  t_car_2.start()
