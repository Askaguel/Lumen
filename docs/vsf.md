# VSF — research / local reference prototype

VSF is an experimental structured-artifact interface. It is not an established
universal standard, production resolver, or an independently certified protocol.

The local reference test uses a canonical JSON artifact of 744 bytes, SHA-256:

`505a0b25f5a816a54304df6e95e5aa022464af9699bcb6c0d752001531f1dc4a`

The private reference implementation checked RFC 8785 canonicalization,
SVG metadata, PNG rendering, QR encoding and decoding with a separate decoder.
This demonstrates a bounded local round trip. It does not demonstrate arbitrary
cross-model interoperability, semantic truth or a deployed resolver. Cross-host
font/rendering reproducibility and independent reproduction remain open.

The public interface concept separates payload identity, transport metadata and
verification results. A hash is an integrity reference, not an authenticity or
rights certificate. Private runtime code and internal role vocabularies are not
part of this public summary.

[Verification status](verification-status.md) · [Home](index.html)
