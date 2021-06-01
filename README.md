## Prerequisites
- Tested on python 3.6.13, ubuntu 18.04 
- Anaconda

## Installation 

```
conda create -n VideoOutpainting python=3.6.13
conda activate VideoOutpainting
conda install pytorch=1.6.0 torchvision=0.7.0 cudatoolkit=10.1 matplotlib tensorboard scipy opencv -c pytorch
pip install tensorflow-gpu==1.15.2
pip install imageio
pip install scikit-image
pip install imageio-ffmpeg
```

- download weights for image completion network from https://github.com/zsyzzsoft/co-mod-gan 
    ./co-mod-gan-places2-050000.pkl

- download weight for RAFT (optical flow) from https://github.com/princeton-vl/RAFT
     ./raft-things.pth

- download weights for COSNet (VOS) from https://github.com/carrierlxk/COSNet
     ./co_attention.pth

## Usage

- Save video frames
```bash
python VidToFrames.py --path ./name.mp4 --outroot ./frames/
```

- Video outpainting:
```bash
cd tool
python video_outpaint.py --path ../frames/ --outroot ../results/frames/ --W_scale 600
```
replace 600 by amount of pixels added to each side.


## Acknowledgments
- Our code is based upon [FGVC](https://github.com/vt-vl-lab/FGVC/).
