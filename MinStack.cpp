#include<iostream>
#include<stack>

using namespace std;

int main()
{

    //Get minimum value in constant time uisng stack
    //this approach will keep min and top element at top of the stack at any time
    //you can perfrom pop operation to remove top
    //you can display what is current min and top
    int q;
    cout << "Enter number of queries: ";
    cin >> q;
    //type 1 x --> insert x in stack
    //type 2 --> pop top
    //type 3 --> value of top and min

    stack<pair<int, int> > st;

    while( q-- )
    {
        cout << "enter query type:\n1. Push 2. Pop 3. Display top and min\n";

        int type;
        cin >> type;
        
        if(type == 1)
        {
            int x;
            cout << "Enter value to insert\n";
            cin >> x;
            
            int mn = x;
            if(!st.empty())
            {
                mn = min(st.top().second, x);

            }
            st.push({x, mn});
        }
        else if( type == 2)
        {
            if(!st.empty())
            {
                st.pop();
            }
            else
            cout << "Stack is already emepty\n";
        }
        else
        {
            if(!st.empty())
            {
                int top = st.top().first;
                int mn = st.top().second;
                cout << "Top: " << top << " Min: " << mn << endl;
            }
            else
            {
                cout << "Stack is empty so can't display top and min\n";
            }
        }

    }
    return 0;
}