!-------------------------------------------------------------------------!
!                                                                         !
! Main program to test subroutine multisource_2dmap.                      !
! For more information, see   multisource_2dmap.f90.                      !
!                                                                         !
!  A. Kuronen, 2022, antti.kuronen@helsinki.fi                            !
!                                                                         !
!-------------------------------------------------------------------------!


program multisource_2dmap_main
  implicit none
  integer,parameter :: rk=8
  real(rk),allocatable :: inten(:,:)
  real(rk) :: d,xmax,rmin
  integer :: sxmin,sxmax,symin,symax,n,rdep
  integer :: i
  character(len=100) :: arg

  if (command_argument_count()/=9) then
     call get_command_argument(0,arg)
     write(0,'(a)') 'usage: '//trim(arg)//' d sxmin sxmax symin symax xmax n rmin rdep'
     stop
  end if

  call get_command_argument(1,arg); read(arg,*) d
  call get_command_argument(2,arg); read(arg,*) sxmin
  call get_command_argument(3,arg); read(arg,*) sxmax
  call get_command_argument(4,arg); read(arg,*) symin
  call get_command_argument(5,arg); read(arg,*) symax
  call get_command_argument(6,arg); read(arg,*) xmax
  call get_command_argument(7,arg); read(arg,*) n
  call get_command_argument(8,arg); read(arg,*) rmin
  call get_command_argument(9,arg); read(arg,*) rdep

  allocate(inten(-n:n,-n:n))
  call multisource_2dmap(d,sxmin,sxmax,symin,symax,xmax,n,rmin,rdep,inten)
  do i=-n,n
     write(10,'(*(g20.10))') inten(i,-n:n)
  end do

end program multisource_2dmap_main
