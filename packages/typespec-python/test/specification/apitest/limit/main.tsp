import "@typespec/rest";
import "@typespec/http";

using TypeSpec.Http;
using TypeSpec.Rest;

@service({
  title: "API Test",
  version: "2023-10-18",
})
@server("https://example.com", "Single server endpoint")
namespace Apitest.Limit;

@route("/apitest/limit")
@put 
op length(
    @minLength(3)
    @maxLength(63)
    @pattern("^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$")
    @path
    name: string,
): NoContentResponse;
