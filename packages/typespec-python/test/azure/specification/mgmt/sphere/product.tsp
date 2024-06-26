import "@azure-tools/typespec-azure-core";
import "@azure-tools/typespec-azure-resource-manager";
import "@typespec/openapi";
import "@typespec/rest";
import "./models.tsp";
import "./catalog.tsp";

using TypeSpec.Rest;
using Azure.ResourceManager;
using Azure.ResourceManager.Foundations;
using TypeSpec.Http;
using TypeSpec.OpenAPI;

namespace Microsoft.AzureSphere;
/**
 * An product resource belonging to a catalog resource.
 */
@parentResource(Catalog)
model Product is Azure.ResourceManager.ProxyResource<ProductProperties> {
  /**
   * Name of product.
   */
  @pattern("^[\\w][\\w\\s]{1,48}[\\w]$|^\\.default$|^\\.unassigned$")
  @path
  @key("productName")
  @segment("products")
  @visibility("read")
  name: string;
}

@armResourceOperations
interface Products {
  /**
   * Get a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name.
   */
  get is ArmResourceRead<Product>;

  /**
   * Create a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name.
   */
  createOrUpdate is ArmResourceCreateOrReplaceAsync<Product>;

  /**
   * Update a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name.
   */
  @parameterVisibility
  update is ArmCustomPatchAsync<Product, ProductUpdate>;

  /**
   * Delete a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name'
   */
  #suppress "deprecated" "For backward compatible"
  #suppress "@azure-tools/typespec-azure-resource-manager/arm-delete-operation-response-codes" "For backward compatible"
  delete is ArmResourceDeleteAsync<Product>;

  /**
   * List Product resources by Catalog
   */
  listByCatalog is ArmResourceListByParent<Product>;

  /**
   * Counts devices in product. '.default' and '.unassigned' are system defined values and cannot be used for product name.
   */
  countDevices is ArmResourceActionSync<Product, void, CountDevicesResponse>;

  /**
   * Generates default device groups for the product. '.default' and '.unassigned' are system defined values and cannot be used for product name.
   */
  generateDefaultDeviceGroups is ArmResourceActionSync<
    Product,
    void,
    ResourceListResult<DeviceGroup>
  >;
}
