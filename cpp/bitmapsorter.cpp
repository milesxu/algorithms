#include <array>
#include <vector>
#include <set>
#include <algorithm>
#include <random>
#include <iostream>

template<size_t N>
class BitmapSorter
{
public:
    BitmapSorter();
    void sort(std::vector<int>& data);

private:
    static const int bitsPerWord = 32;
    static const int shift = 5;
    static const int mask = 0x1f; //31
    std::array<int, 1 + N / bitsPerWord> bitmap;

    void set(int i);
    int test(int i);
    void clear(int i);
};

template<size_t N>
BitmapSorter<N>::BitmapSorter()
{
    std::fill(bitmap.begin(), bitmap.end(), 0);
}

template<size_t N>
void BitmapSorter<N>::sort(std::vector<int>& data)
{
    for (int i : data) set(i);
    data.clear();
    for (size_t i = 0; i < N; i++)
        if (test(i))
            data.push_back(i);
}

template<size_t N>
void BitmapSorter<N>::set(int i)
{
    bitmap[i >> shift] |= (1 << (i & mask));
}

template<size_t N>
int BitmapSorter<N>::test(int i)
{
    return bitmap[i >> shift] & (1 << (i & mask));
}

template<size_t N>
void BitmapSorter<N>::clear(int i)
{
    bitmap[i >> shift] &= ~(1 << (i & mask));
}

int main()
{
    const int N = 1000, n = 20;
    std::mt19937 mt(20141014);
    std::uniform_int_distribution<int> uidn(1, N);
    std::vector<int> data;
    std::set<int> temp;
    while (data.size() < n)
    {
        int j = uidn(mt);
        if (temp.find(j) == temp.end())
        {
            temp.insert(j);
            data.push_back(j);
        }
    }
    std::for_each(data.begin(), data.end(), [](int i){
        std::cout << i << " ";
    });
    std::cout << std::endl;
    BitmapSorter<N> sorter;
    sorter.sort(data);
    for (int i : data)
        std::cout << i << " ";
    std::cout << std::endl;
}