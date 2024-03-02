from django.shortcuts import render


# def get_all_app_models():
#     app_models = {}
#     for app_config in apps.get_app_configs():
#         app_name = app_config.label
#         models = app_config.get_models()
#         model_names = [model.__name__ for model in models]
#         app_models[app_name] = model_names
#     return app_models


# all_app_models = get_all_app_models()
# for app_name, model_names in all_app_models.items():
#     print(f"App Name: {app_name}")
#     print("Model Names:")
#     for model_name in model_names:
#         print(f"\t- {model_name}")
#     print()


def index(request):
    # all_app_models = get_all_app_models()
    # for app_name, model_names in all_app_models.items():
    #     print(f"App Name: {app_name}")
    #     print("Model Names:")
    #     for model_name in model_names:
    #         print(f"\t- {model_name}")
    #         print()
    return render(request, 'base.html')
