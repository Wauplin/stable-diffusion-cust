import functools; print = functools.partial(print, flush=True)
class Restoration():
    def __init__(self) -> None:
        pass

    def load_face_restore_models(self, gfpgan_model_path='./models/gfpgan/GFPGANv1.4.pth'):
        # Load GFPGAN
        gfpgan = self.load_gfpgan(gfpgan_model_path)
        if gfpgan.gfpgan_model_exists:
            print('>> GFPGAN Initialized')
        else:
            print('>> GFPGAN Disabled')
            gfpgan = None

        # Load CodeFormer
        codeformer = self.load_codeformer()
        if codeformer.codeformer_model_exists:
            print('>> CodeFormer Initialized')
        else:
            print('>> CodeFormer Disabled')
            codeformer = None

        return gfpgan, codeformer

    # Face Restore Models
    def load_gfpgan(self, gfpgan_model_path):
        from ldm.invoke.restoration.gfpgan import GFPGAN
        return GFPGAN(gfpgan_model_path)

    def load_codeformer(self):
        from ldm.invoke.restoration.codeformer import CodeFormerRestoration
        return CodeFormerRestoration()

    # Upscale Models
    def load_esrgan(self, esrgan_bg_tile=400):
        from ldm.invoke.restoration.realesrgan import ESRGAN
        esrgan = ESRGAN(esrgan_bg_tile)
        print('>> ESRGAN Initialized')
        return esrgan;
