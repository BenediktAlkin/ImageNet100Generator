# ImageNet subset generator

- Generate a subset (e.g. ImageNet100) from the original ImageNet1K dataset.
  - copy images to seperate folder to use with e.g. ImageFolder from torchvision
  - generate a h5 file and a list of imagenames/labels to use with a [supplied](https://github.com/BenediktAlkin/ImageNetSubsetGenerator/blob/main/imagenet_subset_generator/h5_image_folder.py) `H5ImageFolder`
  - generate a list of imagenames/labels to use with a [supplied](https://github.com/BenediktAlkin/ImageNetSubsetGenerator/blob/main/imagenet_subset_generator/filelist_image_folder.py) `FilelistImageFolder` which accesses the original ImageNet1K dataset but only reads out the images that are actually contained in the subset (avoids duplicate images and saves storage)
- Generate lightweight dummy datasets for development/debugging environments. 
  These dummy datasets have the same classes as the specified version but take only minimal disk space.
- Get readable labels of any ImageNet version ('ice bear' instead of 'n02134084')

# Usage
- `git clone https://github.com/BenediktAlkin/ImageNetSubsetGenerator`
- `cd ImageNetSubsetGenerator`
- `python <SCRIPT> <ARGS>`


## Generate subset

- `python main_subset.py --in1k_path <ImageNet1K_path> --out_path <out_path> --version in100_sololearn --mode imagefolder`
- this will copy the corresponding classes from the `ImageNet1K_path` to `out_path`
- it can then be readily used with e.g. torchvision ImageFolder `subset = ImageFolder(root=<out_path>)`

#### modes
- `imagefolder`: the result will be a folder with a `train` and a `val` directory, each containing subfolders with the classname which then contains the images
- `h5`: a `train.h5` and a `val.h5` file will be generated containing all images. Additionally also the filelist will be generated for faster loading of h5 images
- `filelist` only generate a list of image names that are contained in the subset

#### use only a fraction of the training data
- `--train_fraction_from <train_fraction_from>` with `0 <= train_fraction < 1.0`
- `--train_fraction_to <train_fraction_to>` with `0 < train_fraction_to <= 1.0`
- this will use only the data within these percentages
- the images are sorted beforehand (within each class) so the following command will produce two disjoint sets 
  - `python main_subset.py ... --train_fraction_to 0.5`
  - `python main_subset.py ... --train_fraction_from 0.5`
- to randomly sample the images used for `train_fraction` use specify `--train_fraction_seed`
- limit the maximum number of samples per class by specifying `--max_train_samples_per_class`


## Generate dummy dataset

Generate a lightweight dummy dataset for debugging/development environments.

`python main_dummy_dataset.py --out_path <out_path> --version <VERSION> [--train_size <TRAIN_SIZE>] [--valid_size <VALID_SIZE>] [--resolution_min <RES_MIN>] [--resolution_max <RES_MAX>]`

Optional CLI arguments:
- `--train_size <TRAIN_SIZE>` how many train samples per class
- `--valid_size <VALID_SIZE>` how many validaion samples per class
- `--resolution_min <RESOLUTION_MIN>` each generated dummy sample has a random resolution sampled from `[RESOLUTION_MIN; RESOLUTION_MAX]` (16 by default)
- `--resolution_max <RESOLUTION_MAX>` each generated dummy sample has a random resolution sampled from `[RESOLUTION_MIN; RESOLUTION_MAX]` (16 by default)

## Check classes/samples of dataset

`python main_statistics.py <path>`
```
train n_classes: 1000
valid n_classes: 1000
train n_samples: 1282169
valid n_samples: 50000
train classes: ['n01440764', ...]
valid classes: ['n01440764', ...]
```


# Versions

- `in1k` - original ImageNet1K (only available for generating a dummy dataset based on this version)
- `in100_kaggle` - subset of ImageNet1K with 100
  classes ([source](https://www.kaggle.com/datasets/ambityga/imagenet100))
- `in100_sololearn` - subset of ImageNet1K with 100
  classes ([source](https://github.com/vturrisi/solo-learn/issues/137))
- `in100_sololearn_cv1` - "cross validation split" with `in100_sololearn` as base <br/>
   (100 random classes that don't occour in `in100_sololearn`)
- `in100_sololearn_cv2` - "cross validation split" with `in100_sololearn` as base <br/> 
  (100 random classes excluding `in100_sololearn` and all previous `in100_sololearn_cv` classes)
- `in100_sololearn_cv3` - "cross validation split" with `in100_sololearn` as base <br/>
  (100 random classes excluding `in100_sololearn` and all previous `in100_sololearn_cv` classes)
- `in100_sololearn_cv4` - "cross validation split" with `in100_sololearn` as base <br/>
  (100 random classes excluding `in100_sololearn` and all previous `in100_sololearn_cv` classes)
- `in100_sololearn_cv5` - "cross validation split" with `in100_sololearn` as base <br/> 
  (100 random classes excluding `in100_sololearn` and all previous `in100_sololearn_cv` classes)
- `in100_sololearn_cv6` - "cross validation split" with `in100_sololearn` as base <br/>
  (100 random classes excluding `in100_sololearn` and all previous `in100_sololearn_cv` classes)
- `in100_sololearn_cv7` - "cross validation split" with `in100_sololearn` as base <br/> 
  (100 random classes excluding `in100_sololearn` and all previous `in100_sololearn_cv` classes)
- `in100_sololearn_cv8` - "cross validation split" with `in100_sololearn` as base <br/>
  (100 random classes excluding `in100_sololearn` and all previous `in100_sololearn_cv` classes)
- `in100_sololearn_cv9` - "cross validation split" with `in100_sololearn` as base <br/>
  (100 random classes excluding `in100_sololearn` and all previous `in100_sololearn_cv` classes)
- `in10_m3ae` - classes used for visualization in [M3AE](https://arxiv.org/abs/2205.14204)
- `in200_sololearn_cv0` - concatenation of `in100_sololearn` and `in100_sololearn_cv1`
- `in200_sololearn_cv1` - concatenation of `in100_sololearn_cv2` and `in100_sololearn_cv3`
- `in200_sololearn_cv2` - concatenation of `in100_sololearn_cv4` and `in100_sololearn_cv5`
- `in200_sololearn_cv3` - concatenation of `in100_sololearn_cv6` and `in100_sololearn_cv7`
- `in200_sololearn_cv4` - concatenation of `in100_sololearn_cv8` and `in100_sololearn_cv9`
- `in400_sololearn_cv0` - concatenation of `in100_sololearn`, `in100_sololearn_cv1`, `in100_sololearn_cv2`, `in100_sololearn_cv3`
- `in400_sololearn_cv1` - concatenation of `in100_sololearn_cv4`, `in100_sololearn_cv5`, `in100_sololearn_cv6`, `in100_sololearn_cv7`


## Get class labels
`python main_get_class_labels --version <VERSION>`

`python main_get_class_labels --version in10_m3ae`
```
generating in10_m3ae
classes: ['n01440764', 'n01773797', 'n02071294', 'n02104029', 'n02134084', 'n02484975', 'n02835271', 'n03127747', 'n03492542', 'n03786901']
n01440764: ('tench', 'Tinca tinca')
n01773797: ('garden spider', 'Aranea diademata')
n02071294: ('killer whale', 'killer', 'orca', 'grampus', 'sea wolf', 'Orcinus orca')
n02104029: ('kuvasz',)
n02134084: ('ice bear', 'polar bear', 'Ursus Maritimus', 'Thalarctos maritimus')
n02484975: ('guenon', 'guenon monkey')
n02835271: ('bicycle-built-for-two', 'tandem bicycle', 'tandem')
n03127747: ('crash helmet',)
n03492542: ('hard disc', 'hard disk', 'fixed disk')
n03786901: ('mortar',)
```

## Check if folder is of version
`python main_check_folder_is_version.py --path <PATH_TO_FOLDER> --version <VERSION>`

```
<VERSION>
classes: [...]
<PATH_TO_FOLDER> contains all classes of <VERSION>
SUCCESS
```

## ImageNet-A/ImageNet-R/...
[ImageNet-A](https://github.com/hendrycks/natural-adv-examples)/
[ImageNet-R](https://github.com/hendrycks/imagenet-r)/... only contain samples for a subset of the ImageNet1K classes. 
For easy usage with `torchvision.datasets.ImageFolder` empty folders for classes without samples are created. 
`create_empty_in1k_folders.sh` does exactly that when following the folder structure of ImageNet1K:
```
ImageNet-A/
  create_empty_in1k_folders.sh
  val/
    n01498041
    n01531178
    ...
```