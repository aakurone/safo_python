!----------------------------------------------------------------------!
!                                                                      !
! Planewaves in 2D.                                                    !
! Prints out the interference pattern.                                 !
! Converted the Fortran main program to a subroutine callable from     !
! Python.                                                              !
!                                                                      !
! Compilation:                                                         !
!    f2py -c planewaves.f90 -m planewaves                              !
!                                                                      !
! Usage in Python:                                                     !
!    import numpy as np                                                !
!    import matplotlib.pyplot as plt                                   !
!    import planewaves                                                 !
!    a=planewaves.planewaves(20.0,5,1.0,1000)                          !
!    plt.clf()                                                         !
!    plt.imshow(np.real(a))                                            !
!                                                                      !
!  A. Kuronen, 2022, antti.kuronen@helsinki.fi                         !
!                                                                      !
!----------------------------------------------------------------------!

subroutine planewaves(xmax,nw,k,a,n)
  implicit none
  integer,parameter :: rk=8
  real(rk),parameter :: pi=4.0_rk*atan2(1.0_rk,1.0_rk)
  complex(rk),parameter :: ima=cmplx(0.0_rk,1.0_rk,rk)
  real(rk),intent(in) :: xmax,k
  integer,intent(in) :: nw,n
  complex(rk),intent(out) :: a(n,n)
  complex(rk) :: b(n,n)
  integer :: i,j,l
  real(rk) :: th,x,y,kr,dt,dx
  real(rk),dimension(nw) :: kxa,kya


  dx=xmax/n
  b=0

  dt=2.0_rk*pi/nw
  do i=1,nw
     th=dt*(i-1)
     kxa(i)=k*sin(th)
     kya(i)=k*cos(th)
  end do

  do i=1,n
     x=dx*(i-(n/2+1))
     do j=1,n
        y=dx*(j-(n/2+1))
        do l=1,nw
           kr=x*kxa(l)+y*kya(l)
           b(i,j)=b(i,j)+exp(ima*kr)
        end do
     end do
  end do
  a=b
  return

end subroutine planewaves
