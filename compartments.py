import oci
config = oci.config.from_file()
identity = oci.identity.IdentityClient(config)
compartments = identity.list_compartments(config["tenancy"]).data

