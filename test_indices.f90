program test_indices
  implicit none
  integer :: n,i
  real :: x

  read *, n

  do i=1,n
     x=i-(n/2+1)
     print *,i,x
  end do

end program test_indices
