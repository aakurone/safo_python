!----------------------------------------------------------------------!
!                                                                      !
! Double source interference demo for SäFo.                            !
! Converted the Fortran main program to a subroutine callable from     !
! Python.                                                              !
!                                                                      !
! Compilation:                                                         !
!       f2py -c doublesource_2dmap.f90 -m doublesource_2dmap           !
!                                                                      !
! Usage in Python:                                                     !
!    import numpy as np                                                !
!    import matplotlib.pyplot as plt                                   !
!    import doublesource_2dmap                                         !
!    d=doublesource_2dmap.doublesource_2dmap(2.5,20,101,0.1,False)     !
!    plt.clf()                                                         !
!    plt.imshow(d)                                                     !
!                                                                      !
!  A. Kuronen, 2022, antti.kuronen@helsinki.fi                         !
!                                                                      !
!----------------------------------------------------------------------!



subroutine doublesource_2dmap(d,xmax,n,rmin,rdep,inten)
  implicit none
  integer,parameter :: rk=8
  real(rk),parameter :: pi=4.0_rk*atan2(1.0_rk,1.0_rk)
  real(rk),intent(in) :: d,xmax,rmin
  integer,intent(in) :: rdep,n
  real(rk),intent(out) :: inten(-n:n,-n:n)
  real(rk) :: x,y,phi,r1,r2,dl
  real(rk) :: a,b,tave,dave
  real(rk) :: dx,dy
  integer :: ix,iy
  logical :: rdependence
  
  rdependence=rdep>0

  dx=xmax/n
  dy=dx
  inten=0.0

  do ix=-n,n
     do iy=-n,n
        x=dx*ix
        y=dy*iy
        r1=sqrt((x+d/2.0)**2+y**2)
        r2=sqrt((x-d/2.0)**2+y**2)
        if (r1>rmin .and. r2>rmin) then
           if (rdependence) then
              a=1/r1
              b=1/r2
           else
              a=1
              b=1
           end if
           dl=r2-r1
           phi=2*pi*dl
           dave=(r1+r2)/2.0
           tave=(a**2+b**2+2*a*b*cos(phi))/2.0
           if (rdependence) then
              tave=tave*dave**2
           end if
        else
           tave=0.0
        end if
        inten(ix,iy)=inten(ix,iy)+tave
     end do
  end do

end subroutine doublesource_2dmap
