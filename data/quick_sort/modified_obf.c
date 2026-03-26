#include <stdio.h>

void sw(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int pt(int a[], int l, int h)
{
    int pv = a[h], si = l - 1, i;
    for (i = l; i < h; i++)
        if (a[i] <= pv)
        {
            si++;
            sw(&a[si], &a[i]);
        }
    sw(&a[si + 1], &a[h]);
    return si + 1;
}

void qs(int a[], int l, int h)
{
    if (l < h)
    {
        int pi = pt(a, l, h);
        qs(a, l, pi - 1);
        qs(a, pi + 1, h);
    }
}
