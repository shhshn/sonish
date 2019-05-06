#include <iostream>
#include <vector>
#include <unordered_map>

int main() {
  std::cout << "Hello and, again!" << std::endl;
  auto l = std::vector<int>{3, 2};
  l.push_back(1);
  for (auto x : l)
    std::cout << x << std::endl;
  auto d = std::unordered_map<int, const char *>{{4, "HUGE"}, {5, "SUCESS"}};
  std::cout << d[5] << std::endl;
  return 0;
}
