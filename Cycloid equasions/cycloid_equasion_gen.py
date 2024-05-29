import argparse
# N - Number of rollers
# Rr - Radius of the roller
# R - Radius of the rollers PCD - Pitch Circle Diameter
# E - Eccentricity - offset from input shaft to a cycloidal disk



# x = (R*cos(t))-(Rr*cos(t+arctan(sin((1-N)*t)/((R/(E*N))-cos((1-N)*t)))))-(E*cos(N*t))
# y = (-R*sin(t))+(Rr*sin(t+arctan(sin((1-N)*t)/((R/(E*N))-cos((1-N)*t)))))+(E*sin(N*t))

def get_X_equasion(R,Rr,N,E):
  R_equasion=f"1 mm * ( {R} ul * cos(1 rad * t) ) - 1 mm * ( {Rr} ul * cos(1 rad * t + atan(sin(1 rad * ( 1 ul - {N} ul ) * t) / ( ( {R} ul / ( {E} ul * {N} ul ) ) - cos(1 rad * ( 1 ul - {N} ul ) * t) ))) ) - 1 mm * ( {E} ul * cos(1 rad * {N} ul * t) )"
  return R_equasion

def get_Y_equasion(R,Rr,N,E):
  Y_equaison =f"1 mm * ( {R} ul * sin(1 rad * t) ) - 1 mm * ( {Rr} ul * sin(1 rad * t + atan(sin(1 rad * ( 1 ul - {N} ul ) * t) / ( ( {R} ul / ( {E} ul * {N} ul ) ) - cos(1 rad * ( 1 ul - {N} ul ) * t) ))) ) - 1 mm * ( {E} ul * sin(1 rad * {N} ul * t) )"
  return Y_equaison


def main():
  parser = argparse.ArgumentParser(description='Cycloid Equation Generator')
  parser.add_argument('-R', type=float, help='Radius of the  outer rollers PCD')
  parser.add_argument('-Rr', type=float, help='Radius of the single roller')
  parser.add_argument('-N', type=int, help='Number of rollers  Ration of the gearbox is N-1')
  parser.add_argument('-E', type=float, help='Eccentricity - offset from input shaft to a cycloidal disk')
  args = parser.parse_args()

  if args.R is None or args.Rr is None or args.N is None or args.E is None:
    parser.print_help()
  else:
    R = args.R
    Rr = args.Rr
    N = args.N
    E = args.E

    R_equasion = get_X_equasion(R, Rr, N, E)
    Y_equaison = get_Y_equasion(R, Rr, N, E)

    print(f"X equation: \n{R_equasion}")
    print(f"Y equation: \n{Y_equaison}")

if __name__ == '__main__':
  main()
