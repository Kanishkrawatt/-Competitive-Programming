#include <bits/stdc++.h>

using namespace std;
#define vi vector<int>
void print(std::vector <int> const &a) {
   for(int i=0; i < a.size(); i++)
   cout << a.at(i) << ' ';
}
int main()
{
    vi block;
    int Number_of_queries, type, color1, color2;
    cin >> Number_of_queries;
    for (int i = 0; i < Number_of_queries; i++)
    {
        cin >> type;
        if (type == 1)
        {
            cin >> color1;
            block.push_back(color1);
        }
        else
        {
            cin >> color1;
            cin >> color2;
            if (block.begin() != block.end())
            {
                while (find(block.begin(), block.end(), color1) != block.end())
                {
                    replace(block.begin(), block.end(), color1, color2);
                }
            }
        }
    }
    print(block);
}