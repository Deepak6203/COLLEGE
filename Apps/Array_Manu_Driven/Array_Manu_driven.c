#include<stdio.h>
#include<conio.h>
int main()
{
	int arr[100] ,ch ,i,n, m,  pos,  j,tmp;
	
	do{
		system("cls");
		printf("----------------------------------");
		printf("\n1.CREATE DATA");
		printf("\n2.DISPAY DATA");
		printf("\n3.APPEND DATA");
		printf("\n4.COUNT DATA");
		printf("\n5.SEARCH BY POSITION");
		printf("\n6.UPDATE BY POSITION");
		printf("\n7.DELETE BY POSITION");
		printf("\n8.REVERS DATA");
		printf("\n9.SORT DATA ASCENDING");
		printf("\n10.SORT DATA DESCENDING");
		printf("\n0.EXIT");
		printf("\n----------------------------------");
		printf("\nENTER Your Choice : ");
		scanf("%d",&ch);
		
		switch(ch)
		{
			case 1:
				printf("Enter how many nos you waant :\n ");
				scanf("%d",&n);
				for(i=0; i<n; i++)
				{
					printf("Enter No : ");
					scanf("%d",&arr[i]);
				}
			break;
			case 2:
				printf("Your Data\n");
				for(i=0; i<n; i++)
				{
					printf("=>%d ",arr[i]);	
				}
			break;
			case 3:
				printf("Enter how many nos you waant : ");
				scanf("%d",&m);
				for(i=n; i<n+m; i++)
				{
					printf("Enter No : ");
					scanf("%d",&arr[i]);
				}
				n = n + m;
			break;
			case 4:
				printf("\nTotal no Of Data = %d",n);
			break;	
			case 5:
				printf("Enter Position to Search : ");
				scanf("%d",&pos);
				
				if(pos>n){
					printf("Position must be less than or equal %d",n);
				}
				else{
					printf("Element at %d Position = %d",pos,arr[pos-1]);
				}
			break;
			case 6:
				printf("Enter Position to Update : ");
				scanf("%d",&pos);
				
				if(pos>n){
					printf("Position must be less than or equal %d",n);
				}
				else{
						printf("Element at %d Position = %d",pos,arr[pos-1]);
						printf("\nEnter New no : ");
						scanf("%d",&arr[pos-1]);
							printf("Element at %d Position = %d",pos,arr[pos-1]);
				}
			break;
			case 7:
				printf("Enter Position to Delete : ");
				scanf("%d",&pos);
				
				if(pos>n){
					printf("Position must be less than or equal %d",n);
				}
				else{
						printf("%d Is Delete Succesfully...!",arr[pos-1]);
						for(i=pos-1; i<n-1; i++){
							arr[i]=arr[i+1];
						}
						n--;
				}
			break;
			case 8:
				printf("\nREVERS DATA\n");
				for(i=n-1; i>=0; i--){
					printf("%d ",arr[i]);
				}
			break;
			case 9:
				for(i=0; i<n; i++){
					for(j=i+1; j<n; j++){
						if(arr[i]>arr[j]){
							tmp = arr[i];
							arr[i] =arr[j];
							arr[j]=tmp;
						}
					}	
				}
				printf("\nSorted Data\n");
				for(i=0; i<n; i++){
					printf("%d ",arr[i]);
				}
			break;
			case 10:
				for(i=0; i<n; i++){
					for(j=i+1; j<n; j++){
						if(arr[i]<arr[j]){
							tmp = arr[i];
							arr[i] =arr[j];
							arr[j]=tmp;
						}
					}	
				}
				printf("\nSorted Data\n");
				for(i=0; i<n; i++){
					printf("%d ",arr[i]);
				}
			break;
		}
		printf("\n\n");
		system("pause");
	}while(ch!=0);
}
