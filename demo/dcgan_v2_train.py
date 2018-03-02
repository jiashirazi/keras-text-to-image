from keras_text_to_image.library.dcgan_v2 import DCGanV2
from keras_text_to_image.library.utility.img_cap_loader import load_normalized_img_and_its_text
import numpy as np
from random import shuffle


def main():
    seed = 42

    np.random.seed(seed)

    img_dir_path = './data/pokemon/img'
    txt_dir_path = './data/pokemon/txt'
    model_dir_path = './models'

    img_width = 64
    img_height = 64
    img_channels = 3

    image_label_pairs = load_normalized_img_and_its_text(img_dir_path, txt_dir_path, img_width=img_width, img_height=img_height)

    shuffle(image_label_pairs)

    gan = DCGanV2()
    gan.img_width = img_width
    gan.img_height = img_height
    gan.img_channels = img_channels
    gan.glove_source_dir_path = './very_large_data'

    batch_size = 16
    epochs = 1000
    gan.fit(model_dir_path=model_dir_path, image_label_pairs=image_label_pairs,
            snapshot_dir_path='./data/snapshots',
            snapshot_interval=100,
            batch_size=batch_size,
            epochs=epochs)


if __name__ == '__main__':
    main()
