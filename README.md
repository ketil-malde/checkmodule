# Checking components

Contents:

- `check.py`: check a component
- `checkall.sh`: check all components in `modules.txt`
- `modules.txt`: list of components (git repositories)

## Examples

`Data.py`, `Model.py`, and `Project.py` are skeleton code for how the
three types of components can (should) be structured.  Any component
repository should only provide one of these.

## Example repositories

### Segmentation of blue mussel drone images

        git@github.com:ketil-malde/blue-mussel-drone-testdata

Data directory copies files from server using `rsync`, processes
CSV-formatted polygons to generate mask images.  Unannotated images are
placed in a `test` folder.

    --branch standardize git@github.com:ketil-malde/Pytorch-UNet

Milesial' Unet implementation, tailored to run in a Docker and
train on standard data.

    git@github.com:ketil-malde/unet-blue-mussel-images

Project repository, tying everything together.

### Recognizing fish with Yolo v5

Repositories:

    git@github.com:ketil-malde/yolov5-corkwing-images
    git@github.com:ketil-malde/corkwing-data
    git@github.com:ketil-malde/yolov5

Project, Data, and Model repositories for processing corkwing wrasse
images, converting polygon XML annotations into pixel masks and
bounding box annotations.  The latter is used to train Ultralytics'
Yolo v5 implementation.



