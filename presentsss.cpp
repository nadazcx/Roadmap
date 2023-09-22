#include <iostream>

int main(){
		int n,i;
	int p[n];
	int t[n];
	std::cin>>n;
	for (i=0;i<n;i++){
		std::cin >> p[i];
	//printf("i+1 %d p [i]%d   \n",i+1,p[i]);
		t[p[i]-1]=i+1;
	}
	for(i=0;i<n;i++){
		std::cout<<t[i]<<" ";
	}
	
	return 1;
}
