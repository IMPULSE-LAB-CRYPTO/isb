#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>

int main() {
    //Запускать с GDB online debugger
    // Инициализация генератора случайных чисел. Зависит от времени с 1970 года
    std::srand(std::time(0));
    std::ofstream outfile("random_seq_cpp.txt");

    for (int i = 0; i < 128; ++i) {
        int bit = std::rand() % 2;
        outfile << bit;
    }

    outfile.close();
    std::cout << "save to random_seq_cpp.txt" << std::endl;
    return 0;
}
