from PIL import Image
import numpy as np
import matplotlib.pyplot as plt



def edge(im_black):
 
    p,q = im_black.shape
    out3 = np.zeros((p,q))
    for i in range(3,p-3):
        for j in range(3,q-3):
            s1 = im_black[i-3,j]
            s2 = im_black[i-2,j-1]
            s3 = im_black[i-2,j]
            s4 = im_black[i-2,j+1]
            s5 = im_black[i-1,j-2]
            s6 = im_black[i-1,j-1]
            s7 = im_black[i-1,j]
            s8 = im_black[i-1,j+1]
            s9 = im_black[i-1,j+2]
            s10 = im_black[i,j-3]
            s11 = im_black[i,j-2]
            s12 = im_black[i,j-1]
            s13 = im_black[i,j]
            s14 = im_black[i,j+1]
            s15 = im_black[i,j+2]
            s16 = im_black[i,j+3]
            s17 = im_black[i+1,j-2]
            s18 = im_black[i+1,j-1]
            s19 = im_black[i+1,j]
            s20 = im_black[i+1,j+1]
            s21 = im_black[i+1,j+2]
            s22 = im_black[i+2,j-1]
            s23 = im_black[i+2,j]
            s24 = im_black[i+2,j+1]
            s25 = im_black[i+3,j]
            #sum3 = 98*s13-24*(s7+s12+s14+s19)-0.1*(s1+s2+s3+s4+s5+s6+s8+s9+s10+s11+s15+s16+s17+s18+s20+s21+s22+s23+s24+s25)
            #sum3 = 10*s13-2*(s7+s12+s14+s19)-0.1*(s1+s2+s4+s5+s6+s8+s9+s10+s11+s15+s16+s17+s18+s20+s21+s22+s23+s24+s25)
            #sum3 = 30*s13-7*(s7+s12+s14+s19)-0.1*(s1+s2+s4+s5+s6+s8+s9+s10+s11+s15+s16+s17+s18+s20+s21+s22+s23+s24+s25)
            #sum3 = 50*s13-12*(s7+s12+s14+s19)-0.1*(s1+s2+s4+s5+s6+s8+s9+s10+s11+s15+s16+s17+s18+s20+s21+s22+s23+s24+s25)
            sum3 = 18*s13-4*(s7+s12+s14+s19)-0.1*(s1+s2+s4+s5+s6+s8+s9+s10+s11+s15+s16+s17+s18+s20+s21+s22+s23+s24+s25)
            #sum3 = 98*s13-24.5*(s7+s12+s14+s19)-0*(s1+s2+s4+s5+s6+s8+s9+s10+s11+s15+s16+s17+s18+s20+s21+s22+s23+s24+s25)
            #sum3 = 17*s13-3.75*(s7+s12+s14+s19)-0.1*(s1+s2+s4+s5+s6+s8+s9+s10+s11+s15+s16+s17+s18+s20+s21+s22+s23+s24+s25)
            #sum3 = 17.5*s13-3.875*(s7+s12+s14+s19)-0.1*(s1+s2+s4+s5+s6+s8+s9+s10+s11+s15+s16+s17+s18+s20+s21+s22+s23+s24+s25)
            #sum3 = 12*s13-2.5*(s7+s12+s14+s19)-0.1*(s1+s2+s4+s5+s6+s8+s9+s10+s11+s15+s16+s17+s18+s20+s21+s22+s23+s24+s25)
            #sum3 = 15*s13-3.25*(s7+s12+s14+s19)-0.1*(s1+s2+s4+s5+s6+s8+s9+s10+s11+s15+s16+s17+s18+s20+s21+s22+s23+s24+s25)
            #sum3 = 14*s13-3*(s7+s12+s14+s19)-0.1*(s1+s2+s4+s5+s6+s8+s9+s10+s11+s15+s16+s17+s18+s20+s21+s22+s23+s24+s25)
            #sum3 = 13*s13-3.25*(s7+s12+s14+s19)-0.1*(s1+s2+s4+s5+s6+s8+s9+s10+s11+s15+s16+s17+s18+s20+s21+s22+s23+s24+s25)
            #sum3 = 12*s13-2.25*(s7+s12+s14+s19)-0.15*(s1+s2+s4+s5+s6+s8+s9+s10+s11+s15+s16+s17+s18+s20+s21+s22+s23+s24+s25)
            out3[i,j]=1./(1+np.exp(-(sum3-0.5)*100))
            
    return out3

