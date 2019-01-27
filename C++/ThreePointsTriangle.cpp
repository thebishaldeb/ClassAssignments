// Given Three Points, we need to determine if it forms a triangle.
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	float x1, x2, x3, y1, y2, y3,a,b,c;
	cout << "\nEnter first point: ";
	cin >> x1 >> y1;
	cout << "\nEnter second point: ";
	cin >> x2 >> y2;
	cout << "\nEnter third point: ";
	cin >> x3 >> y3;
	a = pow(x2-x1,2) - pow(y2-y1,2);
	b = pow(x3-x2,2) - pow(y3-y2,2);
	c = pow(x3-x1,2) - pow(y3-y1,2);
	
	if((a==b+c)&&(b==a+c)&&(c==a+b))
		cout << "\nThe points form a triangle";
	else
		cout << "\nThe points do not form a triangle";
	
	return 0;
}
