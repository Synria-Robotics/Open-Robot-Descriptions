from openrd import get_model_path
import argparse


def main(args):
    """Get robot model file path."""
    print(f"Robot name: {args.name}")
    if args.version:
        print(f"Robot version: {args.version}")
    if args.variant:
        print(f"Variant: {args.variant}")
    
    try:
        model_path = get_model_path(
            args.name, 
            version=args.version if args.version else None,
            variant=args.variant if args.variant else None,
            model_format=args.model_format
        )
        print(f"Model path: {model_path}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get robot model file path"
    )
    parser.add_argument("--name", type=str, required=True, help="Robot name (e.g., 'bruce', 'unitree_g1')")
    parser.add_argument("--version", type=str, default=None, help="Robot version (optional)")
    parser.add_argument("--variant", type=str, default=None, help="Variant name (optional, required for some like 'smpl')")
    parser.add_argument(
        "--model_format",
        type=str,
        default="urdf",
        choices=["urdf", "mjcf"],
        help="Model format: 'urdf' or 'mjcf' (default: 'urdf')"
    )
    args = parser.parse_args()

    main(args)


