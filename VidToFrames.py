import cv2
import argparse

def mp4ToFrames(args):
    vidcap = cv2.VideoCapture(args.path)
    success,image = vidcap.read()
    count = 0
    while success:
      cv2.imwrite(args.outroot+"frame%05d.jpg" % count, image)     # save frame as JPEG file      
      success,image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1
      
  
  
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default='../data/tennis', help="dataset for evaluation")
    parser.add_argument('--outroot', default='../result/', help="output directory") 
    mp4ToFrames(parser.parse_args())
  
