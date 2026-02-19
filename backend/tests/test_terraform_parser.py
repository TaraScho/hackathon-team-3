import pytest
from pathlib import Path
from app.parsers.terraform import TerraformParser
from app.parsers.base import NormalizedResource
from app.models import ResourceType


@pytest.fixture
def terraform_parser():
    return TerraformParser()


@pytest.fixture
def sample_terraform_file():
    return Path(__file__).parent / "fixtures" / "terraform" / "main.tf"


def test_parse_terraform_file(terraform_parser, sample_terraform_file):
    """Test parsing Terraform file into normalized resources."""
    resources = terraform_parser.parse_file(sample_terraform_file)

    assert len(resources) == 2
    assert all(isinstance(r, NormalizedResource) for r in resources)

    web_instance = next(r for r in resources if r.resource_id == "aws_instance.web")
    assert web_instance.resource_type == ResourceType.TERRAFORM
    assert web_instance.properties["ami"] == "ami-0c55b159cbfafe1f0"
    assert web_instance.properties["instance_type"] == "t2.micro"
    assert web_instance.metadata["tags"]["Name"] == "web-server"


def test_validate_terraform_syntax(terraform_parser, sample_terraform_file):
    """Test Terraform syntax validation."""
    assert terraform_parser.validate_syntax(sample_terraform_file) is True

    # Test invalid file
    invalid_file = Path(__file__).parent / "fixtures" / "terraform" / "invalid.tf"
    invalid_file.parent.mkdir(parents=True, exist_ok=True)
    with open(invalid_file, 'w') as f:
        f.write("invalid { syntax")

    assert terraform_parser.validate_syntax(invalid_file) is False
