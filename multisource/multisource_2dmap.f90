!-------------------------------------------------------------------------!
!                                                                         !
! Multiple sources' interference demo for SäFo.                           !
! Sources a positioned in a square lattice with lattice constant d        !
! and in the interval [sxmin,sxmax],[symin,symax] in x and y.             !
!                                                                         !
! Subroutine callable from Python.                                        !
!                                                                         !
! Compilation as a Python module:                                         !
!  f2py --f90flags=-O2 -c multisource_2dmap.f90 -m multisource_2dmap      !
!                                                                         !
! For Python usage, see file multrisource.py.                             !
!                                                                         !
!  A. Kuronen, 2022, antti.kuronen@helsinki.fi                            !
!                                                                         !
!-------------------------------------------------------------------------!



subroutine multisource_2dmap(d,sxmin,sxmax,symin,symax,xmax,n,rmin,rdep,inten)
  implicit none
  integer,parameter :: rk=8
  real(rk),parameter :: pi=4.0_rk*atan2(1.0_rk,1.0_rk)
  real(rk),intent(in) :: d,xmax,rmin
  integer,intent(in) :: sxmin,sxmax,symin,symax,rdep,n
  real(rk),intent(out) :: inten(-n:n,-n:n)
  real(rk) :: x,y,r,sx,sy,dx,dy,ampl
  real(rk) :: s1,s2,s3,W,E
  integer :: ix,iy,isx,isy
  logical :: rdependence,tooclose
  character(len=80) :: fmi='(a,i0)',fmr='(a,f10.4)'
  
  rdependence=rdep>0
  dx=xmax/n
  dy=dx
  inten=0.0

  ! print *
  ! print '(a)','----------------------------------'
  ! print fmr,'d     ',d
  ! print fmi,'sxmin ',sxmin
  ! print fmi,'sxmax ',sxmax
  ! print fmi,'symin ',symin
  ! print fmi,'symax ',symax
  ! print fmr,'xmax  ',xmax
  ! print fmi,'n     ',n
  ! print fmr,'rmin  ',rmin
  ! print fmi,'rdep  ',rdep
  ! print '(a)','----------------------------------'
  ! print *
  
  xloop: do ix=-n,n
     yloop: do iy=-n,n

        x=dx*ix
        y=dy*iy
        s1=0.0
        s2=0.0
        s3=0.0        
        
        sxloop: do isx=sxmin,sxmax
           syloop: do isy=symin,symax
              tooclose=.false.
              sx=d*isx
              sy=d*isy
              r=sqrt((x-sx)**2+(y-sy)**2)
              if (r<rmin) then
                 tooclose=.true.
                 exit sxloop
              end if
              if (rdependence) then
                 E=1.0/r
              else
                 E=1.0
              end if
              s1=s1+E*sin(pi*r)*cos(pi*r)
              s2=s2+E*(cos(pi*r))**2
              s3=s3+E
           end do syloop
        end do sxloop

        if (.not.tooclose) then
           W = 2*S1**2 + 2*S2**2 - 2*S2*S3 + 0.5*S3**2
           inten(ix,iy)=W
        end if

     end do yloop
  end do xloop

end subroutine multisource_2dmap
