import "@typespec/http";
import "@azure-tools/typespec-azure-core";

using TypeSpec.Http;
using Azure.Core;

@doc("Test for pageable")
@service({
    title: "Test for pageable",
})
namespace Pageable;

@friendlyName("{name}ListResults", T)
@pagedResult
model ResponsePage<T> {
    @items
    @doc("List of items.")
    items: T[];

    @nextLink
    @doc("Link to fetch more items.")
    nextLink?: string;
}

@doc("Error")
@error
model Error {
    @doc("Error code")
    code: int32;

    @doc("Error message")
    message: string;
}

@doc("User")
model User {
    @doc("User id")
    id: int64;

    @doc("User name")
    name: string;
}

@route("/users")
@get
@doc("List users")
op list(
    @query @doc("Name filter") nameFilter: string
): ResponsePage<User> | Error;
